import React, { useEffect, useState } from "react";
import axios from "axios";

const LecturerDashboard = () => {
    const [user, setUser] = useState(null);

    useEffect(() => {
        // Fetch user details
        axios
            .get("/api/current-user/")
            .then((response) => {
                setUser(response.data);
            })
            .catch((error) => {
                console.error("Error fetching user:", error);
            });
    }, []);

    if (!user) return <p>Loading...</p>;

    return (
        <div>
            <h1>Welcome, {user.first_name}</h1>
            <p>This is the Lecturer Dashboard</p>
        </div>
    );
};

export default LecturerDashboard;
