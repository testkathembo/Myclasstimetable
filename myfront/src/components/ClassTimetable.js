import React, { useEffect, useState } from "react";
import axios from "axios";

const ClassTimetable = () => {
  const [timetable, setTimetable] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTimetable = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/school/api/timetables/");
        setTimetable(response.data);
      } catch (err) {
        console.error("Error fetching timetable:", err);
        setError("Failed to load timetable data");
      } finally {
        setLoading(false);
      }
    };

    fetchTimetable();
  }, []);

  if (loading) {
    return <p>Loading timetable...</p>;
  }

  if (error) {
    return <p style={{ color: "red" }}>{error}</p>;
  }

  return (
    <div>
      <h1 style={{ textAlign: "center" }}>Class Timetable</h1>
      <table
        border="1"
        style={{
          width: "100%",
          borderCollapse: "collapse",
          textAlign: "center",
          marginTop: "20px",
        }}
      >
        <thead>
          <tr>
            <th>ID</th>
            <th>Unit</th>
            <th>Unit Code</th>
            <th>Day</th>
            <th>Classroom</th>
            <th>Time</th>
            <th>Status</th>
            <th>Lecturer</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          {timetable.map((entry) => (
            <tr key={entry.id}>
              <td>{entry.id}</td>
              <td>{entry.unit_name || "N/A"}</td>
              <td>{entry.unit_code || "N/A"}</td>
              <td>{entry.day}</td>
              <td>{entry.classroom_name || "Zoom"}</td>
              <td>{entry.time || "N/A"}</td>
              <td>{entry.status}</td>
              <td>{entry.lecturer_name || "N/A"}</td>
              <td>{entry.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ClassTimetable;
