import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";
import { createReserva, deleteReserva, getReservaById, updateReserva } from "../api/test.api";
import { toast } from "react-hot-toast";

export function FormReserva() {
    const {
        register,
        handleSubmit,
        formState: { errors },
        setValue,
    } = useForm();
    const navigate = useNavigate();
    const params = useParams();

    const onSubmit = handleSubmit(async (data) => {
        if (params.id) {
            await updateReserva(params.id, data);
            toast.success("Reserva actualizada", {
                position: "bottom-right",
                style: {
                    background: "#101010",
                    color: "#fff",
                },
            });
        } else {
            await createReserva(data);
            toast.success("Nueva Reserva agregada", {
                position: "bottom-right",
                style: {
                    background: "#101010",
                    color: "#fff",
                },
            });
        }

        navigate("/reservas");
    });

    useEffect(() => {
        async function loadReserva() {
            if (params.id) {
                const { data } = await getReservaById(params.id);

                console.log(data)

                setValue("date", data.date);
            }
        }

        loadReserva();
    }, []);

    return (
        <div className="max-w-xl mx-auto">
            <form onSubmit={onSubmit} className="bg-zinc-800 p-10 rounded-lg mt-2">
                <input
                    type="date"
                    placeholder="Fecha"
                    {...register("date", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                    autoFocus
                />

                {errors.date && <span>El campo Fecha es requerido</span>}

                <button className="bg-indigo-500 p-3 rounded-lg block w-full mt-3">
                    Guardar
                </button>
            </form>

            {params.id && (
                <div className="flex justify-end">
                    <button
                        className="bg-red-500 p-3 rounded-lg w-48 mt-3"
                        onClick={async () => {
                            const accepted = window.confirm("¿Esta seguro que desea borrar la Reserva?");
                            if (accepted) {
                                await deleteReserva(params.id);
                                toast.success("Reserva removida", {
                                    position: "bottom-right",
                                    style: {
                                        background: "#101010",
                                        color: "#fff",
                                    },
                                });
                                navigate("/reservas");
                            }
                        }}
                    >
                        Borrar
                    </button>
                </div>
            )}
        </div>
    );
}