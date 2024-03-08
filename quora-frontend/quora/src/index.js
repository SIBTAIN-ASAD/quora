import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import { AuthProvider } from './contexts/AuthContext';
import rootReducer from './redux/reducers/userReducer';

import './index.css';
import App from './components/pages/App';

// Create Redux store
const store = configureStore({
  reducer: rootReducer, // Pass your combined reducers here
  // Add any additional middleware or configurations if needed
});

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <AuthProvider>
        <App />
      </AuthProvider>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
