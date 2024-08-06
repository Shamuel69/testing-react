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
            <Text className={'${focused ? font-PMedium} text-xs'}>{name}</Text>
        </View>
    )
}

function TabLayout() {
  return (
    <>
        <Tabs screenOptions={{ tabBarShowLabel: false }}>
            <Tabs.Screen
                name="home"
                options={{ 
                    title: "Home",
                    headerShown: false,
                    tabBarIcon: ({color, focused}) => (
                        <TabIcon
                            icon={icons.icon}
                            color={color}
                            name="Home"
                            focused={focused}></TabIcon>
                    )
                }}
            />
        </Tabs>
    </>
  )
}

export default TabLayout