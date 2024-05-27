import { Link } from "react-router-dom";

export function Navigation() {
    return (
        <div className="flex justify-between py-3 items-center">
            <Link to="/alumnos">
                <h1 className="font-bold text-3xl mb-4">Cliente Application</h1>
            </Link>
            <button className="bg-indigo-500 p-3 rounded-lg">
                <Link to="/alumnos-create">Crear Alumno</Link>
            </button>
        </div>
    );
}