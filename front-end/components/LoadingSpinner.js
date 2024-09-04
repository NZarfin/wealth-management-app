import React from 'react';
import { ActivityIndicator, View } from 'react-native';
import tailwind from 'tailwind-rn';

const LoadingSpinner = () => (
  <View style={tailwind('flex-1 justify-center items-center')}>
    <ActivityIndicator size="large" color="#0000ff" />
  </View>
);

export default LoadingSpinner;

