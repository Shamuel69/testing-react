import React from 'react'
import { View, Text } from 'react-native'
import { Tabs, Redirect } from 'expo-router';

import { icons } from "../../assets/icons";

const TabIcon = ({icon, color, name, focused}) => {
    return (
        <View>
            <Image source={icon} 
            resizeMode="contain"
            tintColor={color}
            className="w-6 h-6"/>
            <Text>TabIcon</Text>
        </View>
    )
}

function TabLayout() {
  return (
    <>
        <Tabs>
            <Tabs.Screen
                name="home"
                options={{ headerShown: false }}
                tabBarIcon=({focused, color}) => (
                    
                )
        </Tabs>
    </>
  )
}

export default TabLayout