import React, { useState } from 'react';
import { View, Text, TextInput, Alert } from 'react-native';
import HoverButton from '../components/HoverButton';
import tailwind from 'tailwind-rn';
import API_BASE_URL from '../apiConfig';

const LoginScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const data = await response.json();
        // Navigate to Dashboard on success
        navigation.navigate('Dashboard');
      } else {
        // Handle failed login attempt
        const errorData = await response.json();
        Alert.alert('Login Failed', errorData.error || 'Invalid credentials');
      }
    } catch (error) {
      // Handle any network errors or unexpected issues
      Alert.alert('Login Error', 'An unexpected error occurred. Please try again.');
    }
  };

  return (
    <View style={tailwind('flex-1 justify-center items-center bg-gray-100')}>
      <Text style={tailwind('text-2xl font-bold text-gray-800 mb-8')}>Wealth Management</Text>

      <TextInput
        style={tailwind('bg-white px-4 py-2 rounded-lg mb-4 w-4/5')}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
      />
      
      <TextInput
        style={tailwind('bg-white px-4 py-2 rounded-lg mb-8 w-4/5')}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />

      <HoverButton title="Login" onPress={handleLogin} />
    </View>
  );
};

export default LoginScreen;
