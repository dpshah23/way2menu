import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import * as React from 'react';
import { SafeAreaView } from 'react-native';
import { useState } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import home from './Home/home';
import { Alert } from 'react-native';


export default function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = ({navigation}) => {
    console.log('Email:', email);
    console.log('Password:', password);

    const url = 'http://192.168.135.1:8000/login/';

    // Constructing the request body
    const requestBody = {
      email: email,
      password: password
    };

    // Configuring the fetch request
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', // Specify the content type
      },
      body: JSON.stringify(requestBody), // Convert the body to JSON string
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Response:', data);
        if(data.auth==true){
            navigation.navigate('home',{'restaurant_id':data.restaurant_id,'restaurnat_email':data.restaurnat_email,'restaurant_name':data.restaurant_name})
        }
        else{
          Alert.alert("Wrong Credentials","Email And Password Are Incorrect..");
        }
      })
      .catch((error) => {
        
        console.error('Error:', error);
        // Handle errors here
      });
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.inputContainer}>
        <Text style={styles.label}>Email</Text>
        <TextInput
          style={styles.input}
          placeholder="Enter Your Email"
          onChangeText={text => setEmail(text)}
          value={email}
        />
        <Text style={styles.label}>Password</Text>
        <TextInput
          style={styles.input}
          placeholder="Enter Your Password"
          onChangeText={text => setPassword(text)}
          value={password}
          secureTextEntry={true}
        />
        <Button title="Login" onPress={handleLogin} />
      </View>
      <StatusBar style="auto" />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  inputContainer: {
    width: '80%',
    borderWidth: 1,
    borderRadius: 10,
    padding: 20,
  },
  label: {
    marginBottom: 10,
    fontWeight: 'bold',
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 20,
    paddingHorizontal: 10,
    borderRadius: 5,
  },
});
