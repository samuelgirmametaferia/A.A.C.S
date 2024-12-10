import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Text, Button, Alert } from 'react-native';
import { ARView } from 'react-native-ar';

const App = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [arSession, setArSession] = useState(null);

  useEffect(() => {
    const initializeAR = async () => {
      try {
        const session = await ARView.createSession();
        setArSession(session);
        setIsLoading(false);
      } catch (error) {
        Alert.alert('Error', 'Failed to initialize AR session');
      }
    };

    initializeAR();
  }, []);

  const handleTap = (event) => {
    const { x, y } = event.nativeEvent.location;
    // Perform AR interaction based on tap location
    console.log(`Tapped at: x=${x}, y=${y}`);
  };

  if (isLoading) {
    return <Text>Loading AR...</Text>;
  }

  return (
    <View style={styles.container}>
      <ARView
        session={arSession}
        onTap={handleTap}
        style={styles.arView}
      />
      <Button title="Add Historical Marker" onPress={() => { /* Add marker logic here */ }} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  arView: {
    flex: 1,
  },
});

export default App;