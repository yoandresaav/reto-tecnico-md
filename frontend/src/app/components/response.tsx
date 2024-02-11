'use client'


import { useState } from 'react'



// const backendUrl = 'http://localhost:8000/api/';
const backendUrl = `http://${process.env.NEXT_PUBLIC_APP_API_ENDPOINT}/api/`;


type Props = {
    url: string
}

type JsonFormatterProps = {
    data: any
    restart: () => void
}

function JsonFormatter({ data, restart }: JsonFormatterProps) {
    return (
        <div className="relative">
            <button className="absolute bg-sky-700 rounded py-1 hover:bg-sky-600 px-2 right-0 text-white" onClick={restart}>Reset</button>
            <pre className="bg-black text-green-500 p-4 rounded">
                {JSON.stringify(data, null, 2)}
            </pre>
        </div>
    )
}

export default function Response({ url }: Props) {
    const [data, setData] = useState(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    const completeUrl = `${backendUrl}${url}/`

    const restart = () => {
        setData(null)
        setLoading(false)
        setError(null)
    }

    return (
        <div>
        {!error && !data &&
            <button 
                disabled={loading}
                className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'
                onClick={async () => {
                    setLoading(true)
                    setError(null)
                    try {
                        const res = await fetch(completeUrl)
                        const data = await res.json()
                        // pause for 2 seconds only for the purpose of the demo
                        await new Promise(resolve => setTimeout(resolve, 2000))
                        setData(data)
                    } catch (error) {
                        setError(error)
                        setLoading(false)
                        console.error(error)
                        return
                    }
                    setLoading(false)
                }}>
                {loading ?
                    <span className='animate-spin'>Loading 🌀</span> :
                    <span>Get Data 👈</span>
                }
            </button>
        }

        {!loading && !error && data && <JsonFormatter data={data} restart={restart} />}

        {error && <p className='text-red-500'>Error</p>}

        </div>
    )
}
