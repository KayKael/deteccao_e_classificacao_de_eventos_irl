import React, { useState, useEffect } from 'react';
import axios from 'axios';
import io from 'socket.io-client';
import EventList from './components/EventList';
import Notification from './components/Notification';

const socket = io('http://localhost:5000');

const App = () => {
  const [events, setEvents] = useState([]);
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/classify')
      .then(response => {
        setEvents(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the events!', error);
      });

    socket.on('new_event', (data) => {
      setNotifications(data);
    });

    return () => socket.disconnect();
  }, []);

  return (
    <div>
      <h1>Astro Event Detection</h1>
      <EventList events={events} />
      <Notification notifications={notifications} />
    </div>
  );
};

export default App;
