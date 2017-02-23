import React, { Component } from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default class Splash extends Component {

  render() {

      return (
          <View style={styles.container}>
              <View>
              <Text style={styles.text}>Hello World</Text>
              </View>
          </View>
      );
   }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#3498db',
    justifyContent: 'center',
    alignItems: 'center',
  },

  text: {
    color: 'white',
    fontSize: 30,
  },
});
