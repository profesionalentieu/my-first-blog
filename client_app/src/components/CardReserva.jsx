import { useNavigate } from "react-router-dom";

export function CardReserva({ reserva }) {
    const navigate = useNavigate();

    return (
        <div
            className="bg-zinc-800 p-3 hover:bg-zinc-700 hover:cursor-pointer"
            onClick={() => {
                navigate(`/reservas/${reserva.id}`);
            }}
        >
            <h1 className="text-white font-bold uppercase rounded-lg">
                {reserva.id}
            </h1>
            <p className="text-slate-400">{reserva.date}</p>
        </div>
    );
}