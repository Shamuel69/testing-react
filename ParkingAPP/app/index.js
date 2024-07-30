import { StyleSheet, Text, View } from 'react-native'
import React from 'react'
import { StatusBar } from 'expo-status-bar' 

const Home = () => {
    return (
        <View className="text-3xl" style={styles.container}>
        <Text >TEST!</Text>
        <StatusBar style="auto"/>
        
        </View>
    )
}

export default Home

const styles = StyleSheet.create({
    container: {
      flex:1,
      backgroundColor: "blue",
      alignItems: "center",
      justifyContent: "center",
      font: "Poppins-ExtraBold"
    },
    title:{
      fontSize: 10,
      
    }
  })