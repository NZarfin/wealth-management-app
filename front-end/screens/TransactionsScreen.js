import React from 'react';
import { View, Text, FlatList } from 'react-native';
import tailwind from 'tailwind-rn';

const TransactionsScreen = ({ route }) => {
  const { clientId } = route.params;

  const transactions = [
    { id: '1', date: '2024-01-01', amount: 500.00, type: 'credit' },
    { id: '2', date: '2024-01-02', amount: 200.00, type: 'debit' },
  ];

  const renderTransaction = ({ item }) => (
    <View style={tailwind('p-4 bg-white mb-2 rounded-lg')}>
      <Text style={tailwind('text-lg font-semibold text-gray-800')}>{item.type === 'credit' ? 'Credit' : 'Debit'} - ${item.amount}</Text>
      <Text style={tailwind('text-gray-600')}>{item.date}</Text>
    </View>
  );

  return (
    <View style={tailwind('flex-1 bg-gray-100 p-4')}>
      <Text style={tailwind('text-2xl font-bold text-gray-800 mb-4')}>Transactions for Client {clientId}</Text>
      
      <FlatList
        data={transactions}
        keyExtractor={(item) => item.id}
        renderItem={renderTransaction}
      />
    </View>
  );
};

export default TransactionsScreen;

