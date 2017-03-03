/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  Dimensions,
  TouchableHighlight,
} from 'react-native';

import Splash from './Splash';
import Camera from 'react-native-camera';
import api from './API';

export default class testApp extends Component {

  takePicture() {
    this.camera.capture()
      .then((data) => console.log(data))
      .catch(err => console.error(err));
  }

  render() {
    return (
      //<Splash />
      <View>
          <Camera
            ref={(cam) => {
              this.camera = cam;
            }}
            style={styles.preview}
            aspect={Camera.constants.Aspect.fill}>
            <TouchableHighlight onPress={this.takePicture.bind(this)}>
            <View style={{height: 50, width: 50, backgroundColor: '#3498db', borderRadius: 40, margin: 10}}></View>
            </TouchableHighlight>
          </Camera>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
  preview: {
   flexGrow: 1,
   justifyContent: 'flex-end',
   alignItems: 'center',
   height: Dimensions.get('window').height,
   width: Dimensions.get('window').width
 },
});

AppRegistry.registerComponent('testApp', () => testApp);
