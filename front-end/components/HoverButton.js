import React, { useState } from 'react';
import { TouchableOpacity, Text } from 'react-native';
import tailwind from 'tailwind-rn';
import Hoverable from 'react-native-web-hover';

const HoverButton = ({ title, onPress }) => {
  const [hovered, setHovered] = useState(false);

  return (
    <Hoverable onHoverIn={() => setHovered(true)} onHoverOut={() => setHovered(false)}>
      <TouchableOpacity
        onPress={onPress}
        style={[
          tailwind('px-6 py-3 rounded-lg'),
          hovered ? tailwind('bg-blue-700') : tailwind('bg-blue-500'),
        ]}
      >
        <Text style={tailwind('text-white text-lg')}>{title}</Text>
      </TouchableOpacity>
    </Hoverable>
  );
};

export default HoverButton;

