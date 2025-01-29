import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const DashboardRedirect = ({ user }) => {
    const navigate = useNavigate();

    useEffect(() => {
        if (user.role === "ADMIN") {
            navigate("/admin-dashboard");
        } else if (user.role === "LECTURER") {
            navigate("/lecturer-dashboard");
        } else if (user.role === "STUDENT") {
            navigate("/student-dashboard");
        }
    }, [user, navigate]);

    return null; // Or a loading spinner
};

export default DashboardRedirect;
