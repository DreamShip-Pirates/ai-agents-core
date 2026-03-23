#!/usr/bin/env node

/**
 * Context Optimizer
 * Converts deeply nested, verbose JSON payloads into minimal YAML strings optimized for AI context windows.
 * Usage: cat data.json | node context_optimizer.js
 *    or: node context_optimizer.js <file.json>
 */

const fs = require('fs');

// Fields to strip by default to save tokens
const STRIP_FIELDS = new Set(['__v', 'createdAt', 'updatedAt', 'created_at', 'updated_at', 'password', 'hash', 'salt', 'token']);

function toMinimalYaml(obj, indent = '') {
  if (obj === null) return 'null';
  if (typeof obj === 'undefined') return '';
  if (typeof obj !== 'object') {
    if (typeof obj === 'string') {
      // Remove excessive formatting or quotes for simple strings
      if (obj.includes('\\n') || obj.includes('\n')) {
        return `|-\n${obj.split(/\r?\n/).map(line => `${indent}  ${line}`).join('\n')}`;
      }
      return obj; // Plain string
    }
    return String(obj);
  }

  if (Array.isArray(obj)) {
    if (obj.length === 0) return '[]';
    // If array of primitives
    if (obj.every(item => typeof item !== 'object' && item !== null)) {
      return `[${obj.join(', ')}]`;
    }
    let yaml = '';
    for (const item of obj) {
      yaml += `\n${indent}- ${toMinimalYaml(item, indent + '  ').trim()}`;
    }
    return yaml;
  }

  // Object
  const keys = Object.keys(obj).filter(k => !STRIP_FIELDS.has(k) && obj[k] !== null && obj[k] !== undefined && obj[k] !== '');
  if (keys.length === 0) return '{}';

  let yaml = '';
  for (const key of keys) {
    const val = obj[key];
    const valYaml = toMinimalYaml(val, indent + '  ');
    if (typeof val === 'object' && val !== null && (!Array.isArray(val) || val.length > 0)) {
      yaml += `\n${indent}${key}:${valYaml}`;
    } else {
      yaml += `\n${indent}${key}: ${valYaml.trim()}`;
    }
  }
  return yaml;
}

function processData(input) {
  try {
    const data = JSON.parse(input);
    const result = toMinimalYaml(data).trim();
    console.log(result);
  } catch (err) {
    console.error('Error parsing JSON:', err.message);
    process.exit(1);
  }
}

// Read from args or stdin
if (process.argv[2]) {
  const filePath = process.argv[2];
  if (!fs.existsSync(filePath)) {
    console.error('File not found:', filePath);
    process.exit(1);
  }
  const input = fs.readFileSync(filePath, 'utf8');
  processData(input);
} else {
  let input = '';
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', chunk => { input += chunk; });
  process.stdin.on('end', () => {
    if (input.trim()) processData(input);
  });
}
