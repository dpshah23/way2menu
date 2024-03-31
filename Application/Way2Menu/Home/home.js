import React, { useState, useEffect } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Alert } from 'react-native'; // Import Alert from 'react-native'
import { Picker } from '@react-native-picker/picker'; // Import Picker from '@react-native-picker/picker'
import { Feather } from '@expo/vector-icons';
import Constants from 'expo-constants';
import { useRoute } from '@react-navigation/native'; // Import useRoute from '@react-navigation/native'

const API_URL = 'https://api.example.com/orders';

const HomeScreen = () => {
  const route = useRoute(); // Get route object using useRoute hook
  const { restaurant_email, restaurant_id, restaurant_name } = route.params; // Destructure route.params
  const [orders, setOrders] = useState([]);
  const [selectedStatus, setSelectedStatus] = useState('all');

  useEffect(() => {
    // Fetch orders from API
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      const response = await fetch(API_URL);
      const data = await response.json();
      setOrders(data);
    } catch (error) {
      console.error('Error fetching orders:', error);
      Alert.alert('Error', 'Failed to fetch orders. Please try again later.');
    }
  };

  // Other functions remain the same...

  return (
    <View style={styles.container}>
      <View style={styles.navbar}>
        <Text style={styles.navbarText}>{restaurant_name}</Text> {/* Display restaurant name */}
      </View>
      {renderOrders()}
    </View>
  );
};

export default HomeScreen;
