import { StyleSheet, Text, View } from 'react-native'
import { useEffect } from 'react'
import { useFonts } from 'expo-font'
import { SplashScreen, Stack } from 'expo-router'

SplashScreen.preventAutoHideAsync();

const _layout = () => {
  const [fontsLoaded, error] = useFonts({
    "Poppins-Black": require("../assets/css/fonts/Poppins-Black.ttf"),
    "Poppins-BlackItalic": require("../assets/css/fonts/Poppins-BlackItalic.ttf"),
    "Poppins-Bold": require("../assets/css/fonts/Poppins-Bold.ttf"),
    "Poppins-BoldItalic": require("../assets/css/fonts/Poppins-BoldItalic.ttf"),
    "Poppins-ExtraBold": require("../assets/css/fonts/Poppins-ExtraBold.ttf"),
    "Poppins-ExtraBoldItalic": require("../assets/css/fonts/Poppins-ExtraBoldItalic.ttf"),
    "Poppins-ExtraLight": require("../assets/css/fonts/Poppins-ExtraLight.ttf"),
    "Poppins-ExtraLightItalic": require("../assets/css/fonts/Poppins-ExtraLightItalic.ttf"),
    "Poppins-Italic": require("../assets/css/fonts/Poppins-Italic.ttf"),
    "Poppins-Light": require("../assets/css/fonts/Poppins-Light.ttf"),
    "Poppins-LightItalic": require("../assets/css/fonts/Poppins-LightItalic.ttf"),
    "Poppins-Medium": require("../assets/css/fonts/Poppins-Medium.ttf"),
    "Poppins-MediumItlaic": require("../assets/css/fonts/Poppins-MediumItalic.ttf"),
    "Poppins-Regular": require("../assets/css/fonts/Poppins-Regular.ttf"),
    "Poppins-SemiBold": require("../assets/css/fonts/Poppins-SemiBold.ttf"),
    "Poppins-SemiBoldItalic": require("../assets/css/fonts/Poppins-SemiBoldItalic.ttf"),
    "Poppins-Thin": require("../assets/css/fonts/Poppins-Thin.ttf"),
    "Poppins-ThinItalic": require("../assets/css/fonts/Poppins-ThinItalic.ttf"),
  });

  useEffect(() => {
    if(error) throw error;
    if(fontsLoaded) SplashScreen.hideAsync();
  }, [fontsLoaded, error]);
  if(!fontsLoaded && !error) return null;
 
  
  return (
    <Stack>
      <Stack.Screen name="index" options={{ headerShown: false}} />
    </Stack>  
  )
}

export default _layout
