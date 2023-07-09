import './App.css';
import AppHeader from './AppHeader';
import AppFooter from './AppFooter';
import MessageBox from './MessageBox';
import WorkoutContainer from './WorkoutContainer';

const App = () => {

  return (
    <div className="App">
      <AppHeader />
      <WorkoutContainer />
      <MessageBox />
      <AppFooter />
    </div>
  );
}

export default App;
