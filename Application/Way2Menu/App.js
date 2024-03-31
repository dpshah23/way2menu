import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput, Alert } from 'react-native';
import React, { useState } from 'react';
import { SafeAreaView } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';

export default function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleButtonPress = () => {
    // Navigate to Home screen with parameters
    navigateToHomeScreen({ restaurant_id: 70571, restaurnat_email: 'dpshah207@gmail.com', restaurant_name: 'WTF' });
  };

  const handleLogin = () => {
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
        if (data.auth === true) {
          // Navigate to Home screen with parameters
          navigateToHomeScreen(data);
        } else {
          Alert.alert("Wrong Credentials", "Email And Password Are Incorrect..");
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        // Handle errors here
      });
  };

  const navigateToHomeScreen = (params) => {
    // Navigate to Home screen with parameters
    // You should replace 'Home' with the actual name of your home screen component
    // Also, pass the parameters object as the second argument to the navigate function
    navigation.navigate('Home', params);
  };

  return (
    <NavigationContainer>
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
        {/* this is testing purpose */}
        <View>
          <Button title="Go to Screen B" onPress={handleButtonPress} />
        </View>
        {/* this is */}
      </SafeAreaView>
    </NavigationContainer>
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
