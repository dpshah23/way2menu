import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import * as React from 'react';
import { SafeAreaView } from 'react-native';
import { useState } from 'react';
import axios from 'axios';

export default function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    console.log('Email:', email);
    console.log('Password:', password);
    // Add your login logic here

    const cred = {
      'email': email,
      'password': password
    };

    axios.post('http://192.168.135.1:8000/login/', cred, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error(error);
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
