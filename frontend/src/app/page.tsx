
import Response from '@/app/components/response';

type Props = {
  children: React.ReactNode;
}

const QuestionWrapper = ({ children }: Props) => (
  <div className="p-2 my-2">{children}</div>
);

export default async function Home() {

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-2 lg:p-24">


      <section className="w-full lg:px-20">
        <p className="text-2xl font-bold text-center mb-6">Yoandre Saavedra Application</p>

        <QuestionWrapper>
          <p>1. Obtener el número de respuestas contestadas y no contestadas:</p>
          <Response url={'answers/responsed/and/notresponsed'} />
        </QuestionWrapper>

        <QuestionWrapper>
          <p>2. Obtener la respuesta con mayor reputación:</p>
          <Response url={'answers/high-reputation'} />
        </QuestionWrapper>

        <QuestionWrapper>
          <p>3. Obtener la respuesta con menor número de vistas:</p>
          <Response url={'answers/low-number-of-views'} />
        </QuestionWrapper>

        <QuestionWrapper>
          <p>4. Obtener la respuesta más vieja y más actual:</p>
          <Response url={'answers/olds-news'} />
        </QuestionWrapper>

        <QuestionWrapper>
          <p>5. Imprimir en consola del punto 2 al 5:</p>
          <Response url={'answers/prints'} />
        </QuestionWrapper>

        <QuestionWrapper>
          <p>6. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?:</p>
          <Response url={'flights/airport/more/movement'} />
        </QuestionWrapper>

        <QuestionWrapper>
          <p>
            7. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?:
          </p>
          <Response url={'flights/airline/more/flights'} />
        </QuestionWrapper>

        <QuestionWrapper>
          <p>8. ¿En qué día se han tenido mayor número de vuelos?</p>
          <Response url={'flights/day/more/flights'} />
        </QuestionWrapper>

        <QuestionWrapper>
          <p>9. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día?</p>
          <p className="text-sm">Ninguna aerolínea tiene mas de dos vuelos por día en este ejemplo porque los datos SQL dados no los tienen en cuenta, pero agregando a la BD o en los test se puede ver esta funcionalidad.</p>
          <Response url={'flights/airlines/more/two/fligths/by/day'} />
        </QuestionWrapper>
      </section>

    </main>
  );
}
