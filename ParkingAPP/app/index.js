import { StyleSheet, Text, View } from 'react-native'
import React from 'react';
import { Tabs, Redirect, Link } from 'expo-router';

export default function Home(){
    return (
      <View >
        <View style={styles.header}>
            <Text style={styles.title}>SPORM</Text>
        </View>
        <View style={styles.container}>
            <Text style={styles.title}>TEST!</Text>
              <View style={styles.inline_container}>
                <Link href="/home">go to home</Link>
              </View>
        </View>
      </View>
  )
}


const styles = StyleSheet.create({
    
    header: {
      height: 70,
      width: "100%",
      paddingTop: 10,
      justifyContent: "center",
      border: '2px solid #333',
      borderBottomColor: "white",
    },
    container: {
      backgroundColor: '#16082A',
      height:"100%",
      
      alignItems: "center",
      justifyContent: "center",
    },
    title:{
      fontSize: 25,
      fontFamily: "font-PBold",
    },
    inline_container: {
      width: "80%",
      backgroundColor: "red",
      borderRadius: 10,
      borderCurveRadius: 10,
    }
  })