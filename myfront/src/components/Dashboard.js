import React, { useEffect, useState } from "react";
import axios from "axios";

const Dashboard = () => {
    const [user, setUser] = useState(null);

    useEffect(() => {
        axios
            .get("http://127.0.0.1:8000/users/current-user/", { withCredentials: true })
            .then((response) => setUser(response.data))
            .catch((error) => console.error("Error fetching user:", error));
    }, []);

    if (!user) {
        return <p>Loading user data...</p>;
    }

    return (
        <div>
            <h1>Welcome, {user.first_name}!</h1>
            <p>Role: {user.role}</p>
        </div>
    );
};

export default Dashboard;
