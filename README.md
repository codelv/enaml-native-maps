# enaml-native-maps
Charts for enaml-native

Install using the [enaml-native-cli](https://github.com/codelv/enaml-native-cli) (or pip)

```bash

#: Using the enaml-native cli
enaml-native install enaml-native-maps

#: or via pip and link it
pip install enaml-native-maps
enaml-native link enaml-native-maps

```

Then update the manifest in `android/app/src/main/AndroidManifext.xml` to include:

```bash
  
        <!-- If using google maps these two are required.
        You must also define the API key in gradle.properties-->
        <meta-data
            android:name="com.google.android.gms.version"
            android:value="@integer/google_play_services_version" />
        <meta-data
            android:name="com.google.android.geo.API_KEY"
            android:value="@string/google_maps_key" />


```

> Note: Make sure it is __within the `<application>` tags__!  


Now in `android/app/build.gradle` add the `resValue` lines below under the `buildTypes` 
to  tell gradle to pull your key from the `gradle.properties`


```groovy

    buildTypes {
        debug {
            // Add this line
            resValue "string", "google_maps_key",
                    (project.findProperty("GOOGLE_MAPS_API_KEY") ?: "")
        }
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
            // And add this line
            resValue "string", "google_maps_key",
                    (project.findProperty("GOOGLE_MAPS_API_KEY") ?: "")
        }
    }


```

Finally add your `GOOGLE_API_MAPS_KEY=yourapikey` in `android/app/gradle.properties`.


> Note: See https://developers.google.com/maps/documentation/android-api/map-with-marker for help 
and to get an API key. 
 
 