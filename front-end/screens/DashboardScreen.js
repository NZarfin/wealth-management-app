import React, { useEffect, useRef } from 'react';
import { View, Text, FlatList, Animated } from 'react-native';
import tailwind from 'tailwind-rn';
import HoverButton from '../components/HoverButton';

const DashboardScreen = ({ navigation }) => {
  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 1000,
      useNativeDriver: true,
    }).start();
  }, [fadeAnim]);

  const clients = [
    { id: '1', name: 'John Doe', email: 'john@example.com' },
    { id: '2', name: 'Jane Smith', email: 'jane@example.com' },
  ];

  const renderClient = ({ item }) => (
    <HoverButton
      title={`${item.name} - ${item.email}`}
      onPress={() => navigation.navigate('Transactions', { clientId: item.id })}
    />
  );

  return (
    <Animated.View style={[tailwind('flex-1 bg-gray-100 p-4'), { opacity: fadeAnim }]}>
      <Text style={tailwind('text-2xl font-bold text-gray-800 mb-4')}>Clients</Text>
      
      <FlatList
        data={clients}
        keyExtractor={(item) => item.id}
        renderItem={renderClient}
      />
    </Animated.View>
  );
};

export default DashboardScreen;

