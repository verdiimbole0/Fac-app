import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import LoginScreen from "./screens/LoginScreen";
import HomeScreen from "./screens/HomeScreen";
import TutorsScreen from "./screens/TutorsScreen";
import BookSessionScreen from "./screens/BookSessionScreen";
import SessionsScreen from "./screens/SessionsScreen";

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={LoginScreen} options={{ title: "Fac'App" }} />
        <Stack.Screen name="Home" component={HomeScreen} options={{ title: "Accueil" }} />
        <Stack.Screen name="Tutors" component={TutorsScreen} options={{ title: "Choisir un tuteur" }} />
        <Stack.Screen name="BookSession" component={BookSessionScreen} options={{ title: "Réserver un créneau" }} />
        <Stack.Screen name="Sessions" component={SessionsScreen} options={{ title: "Mes sessions" }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
