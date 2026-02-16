---
description: How to set up Firebase App Check debug tokens for testing on real devices
---
# Firebase App Check Debug Token Setup

When running the app via `flutter run` on a **real Android device** (not an emulator), 
Firebase App Check uses a debug provider that requires you to register a debug token 
in Firebase Console.

## Symptoms of Missing Debug Token

- `App attestation failed` errors in logcat
- `PERMISSION_DENIED` errors on Firestore queries
- `Error getting App Check token` warnings

## Steps to Fix

### 1. Run the App

// turbo
```bash
flutter run
```

### 2. Find the Debug Token in Logcat

Look for this line in the terminal output or Android Studio logcat:

```
DebugAppCheckProviderFactory: Debug token: 12345678-1234-1234-1234-123456789012
```

The token is a UUID format like `12345678-1234-1234-1234-123456789012`.

### 3. Register the Token in Firebase Console

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project
3. Navigate to **App Check** in the left sidebar
4. Click on your Android app
5. Click **Manage debug tokens**
6. Click **Add debug token**
7. Paste the token from step 2
8. Give it a descriptive name (e.g., "Samsung S21 Dev Device")
9. Click **Save**

### 4. Restart the App

Stop the app and run again:

// turbo
```bash
flutter run
```

App Check should now work and you'll see:
```
✅ App Check: Debug token obtained successfully
```

## Notes

- Each device generates a unique debug token
- Debug tokens are **not** tied to the app build - they persist across reinstalls
- You can register up to 100 debug tokens per project
- For emulators, the debug token is automatically generated and should work without registration

## For Production

In production builds (`flutter run --release`), the app uses **Play Integrity** (Android) 
or **App Attest** (iOS) which don't require debug tokens. Make sure your release signing 
key's SHA-256 fingerprint is registered in Firebase Console > Project Settings > Your apps.
