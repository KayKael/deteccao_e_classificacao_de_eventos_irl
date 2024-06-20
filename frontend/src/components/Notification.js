import React from 'react';

const Notification = ({ notifications }) => {
  return (
    <div>
      <h2>New Notifications</h2>
      <ul>
        {notifications.map((notification, index) => (
          <li key={index}>
            RA: {notification.ra}, Dec: {notification.dec}, Magnitude: {notification.phot_g_mean_mag}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Notification;
