import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import {store} from './redux/store/store';

import './index.css';
import App from './components/pages/App';


const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={store}>
      {/* <AuthProvider> */}
        <App />
      {/* </AuthProvider> */}
    </Provider>
  </React.StrictMode>
);
