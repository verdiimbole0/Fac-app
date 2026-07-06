import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import LoginScreen from "./screens/LoginScreen";
import RegisterScreen from "./screens/RegisterScreen";
import HomeScreen from "./screens/HomeScreen";
import TutorsScreen from "./screens/TutorsScreen";
import BookSessionScreen from "./screens/BookSessionScreen";
import SessionsScreen from "./screens/SessionsScreen";
import PayScreen from "./screens/PayScreen";
import MessagesScreen from "./screens/MessagesScreen";

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={LoginScreen} options={{ title: "Fac'App" }} />
        <Stack.Screen name="Register" component={RegisterScreen} options={{ title: "Inscription" }} />
        <Stack.Screen name="Home" component={HomeScreen} options={{ title: "Accueil" }} />
        <Stack.Screen name="Tutors" component={TutorsScreen} options={{ title: "Choisir un tuteur" }} />
        <Stack.Screen name="BookSession" component={BookSessionScreen} options={{ title: "Réserver un créneau" }} />
        <Stack.Screen name="Sessions" component={SessionsScreen} options={{ title: "Mes sessions" }} />
        <Stack.Screen name="Pay" component={PayScreen} options={{ title: "Paiement" }} />
        <Stack.Screen name="Messages" component={MessagesScreen} options={{ title: "Messages & documents" }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
