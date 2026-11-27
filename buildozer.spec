[app]
title = Zoya
package.name = zoya
package.domain = org.zoya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,plyer
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,MICROPHONE,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,WAKE_LOCK
android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools_version = 33.0.2
android.ndk = 25b
android.archs = arm64-v8a
[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
