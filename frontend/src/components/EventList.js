import React from 'react';

const EventList = ({ events }) => {
  return (
    <div>
      <h2>Detected Events</h2>
      <ul>
        {events.map(event => (
          <li key={event.source_id}>
            RA: {event.ra}, Dec: {event.dec}, Magnitude: {event.phot_g_mean_mag}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EventList;
