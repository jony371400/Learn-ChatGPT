import './App.css';
import LoginForm from './LoginForm';
import RegistrationForm from './RegistrationForm';
import DeletionForm from './DeletionForm';

function App() {
  return (
    <div className="App">
      <h1>Test Login</h1>
      <LoginForm></LoginForm>
      <RegistrationForm></RegistrationForm>
      <DeletionForm></DeletionForm>
    </div>
  );
}

export default App;