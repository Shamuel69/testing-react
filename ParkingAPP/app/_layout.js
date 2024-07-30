import { StyleSheet, Text, View } from 'react-native'
import { useEffect } from 'react'
import { useFonts } from 'expo-font'
import { SplashScreen, Stack } from 'expo-router'

SplashScreen.preventAutoHideAsync();
 
const Fonts = () => {
  const [fontsLoaded, error] = useFonts({
    "font-PBlack": require("../assets/css/fonts/Poppins-Black.ttf"),
    "font-PBlackItalic": require("../assets/css/fonts/Poppins-BlackItalic.ttf"),
    "font-PBold": require("../assets/css/fonts/Poppins-Bold.ttf"),
    "font-PBoldItalic": require("../assets/css/fonts/Poppins-BoldItalic.ttf"),
    "font-PExtraBold": require("../assets/css/fonts/Poppins-ExtraBold.ttf"),
    "font-PExtraBoldItalic": require("../assets/css/fonts/Poppins-ExtraBoldItalic.ttf"),
    "font-PExtraLight": require("../assets/css/fonts/Poppins-ExtraLight.ttf"),
    "font-PExtraLightItalic": require("../assets/css/fonts/Poppins-ExtraLightItalic.ttf"),
    "font-PItalic": require("../assets/css/fonts/Poppins-Italic.ttf"),
    "font-PLight": require("../assets/css/fonts/Poppins-Light.ttf"),
    "font-PLightItalic": require("../assets/css/fonts/Poppins-LightItalic.ttf"),
    "font-PMedium": require("../assets/css/fonts/Poppins-Medium.ttf"),
    "font-PMediumItlaic": require("../assets/css/fonts/Poppins-MediumItalic.ttf"),
    "font-PRegular": require("../assets/css/fonts/Poppins-Regular.ttf"),
    "font-PSemiBold": require("../assets/css/fonts/Poppins-SemiBold.ttf"),
    "font-PSemiBoldItalic": require("../assets/css/fonts/Poppins-SemiBoldItalic.ttf"),
    "font-PThin": require("../assets/css/fonts/Poppins-Thin.ttf"),
    "font-PThinItalic": require("../assets/css/fonts/Poppins-ThinItalic.ttf"),
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

export default Fonts
