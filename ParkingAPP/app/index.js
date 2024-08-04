import { StyleSheet, Text, View } from 'react-native'
import React from 'react';
import { StatusBar } from 'expo-status-bar'; 
import { Link } from 'expo-router';
export default function Home(){
    return (
        <View style={styles.container}>
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
      backgroundColor: 'rgb(42, 34, 54)',

      flex:1,
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