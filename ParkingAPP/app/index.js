import { StyleSheet, Text, View } from 'react-native'
import React from 'react';
import { LinearGradient } from 'expo-linear-gradient';
import { StatusBar } from 'expo-status-bar'; 
import { Link } from 'expo-router';
export default function Home(){
    return (
      <View>
        <LinearGradient colors={['#18151C','#18151C', '#181028', "#1A1229","#1B112E","#1D1231", '#281649']} style={{height: "100%"}} useAngle={true} angle={45} angleCenter={{x: 2.5, y: 0}}>
        <View style={styles.header}>
            <Text>Parksie</Text>
        </View>
        <View style={styles.container}>
          <Text style={styles.title}>TEST!
            <View style={styles.inline_container}>
            </View>
          </Text>
        </View>
        </LinearGradient>
      </View>
        
      
  )
}


const styles = StyleSheet.create({
    header: {
      width: "100%",
      height: "100%",
      alignItems: "center",
      justifyContent: "center",
      borderBottomColor: "white",
    },
    container: {
      backgroundColor: '#251F30',
      
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