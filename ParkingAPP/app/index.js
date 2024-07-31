import { StyleSheet, Text, View } from 'react-native'
import React from 'react';
import { StatusBar } from 'expo-status-bar'; 
import { Link } from 'expo-router';
import { ../assets/css/color.css };
export default function Home(){
    return (
        <View style={width="100%", height="100%", backgroundColor="#f0f8ff"}>
          <Text style={styles.title} >TEST!
            <View style={styles.inline_container}>

            </View>
          </Text>
        <StatusBar style="auto"/>
        
        </View>
    )
}


const styles = StyleSheet.create({
    container: {
      flex:1,
      backgroundColor: "blue",
      alignItems: "center",
      justifyContent: "center",
    },
    title:{
      fontSize: 35,
      fontFamily: "font-PBold",
    },
    inline_container: {
      width: "80%",
      backgroundColor: "red",
      borderRadius: 10,
      borderCurveRadius: 10,
    }
  })