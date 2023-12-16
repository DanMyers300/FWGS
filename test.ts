import { NextRequest } from 'next/server';
import { Message as VercelChatMessage,
    StreamingTextResponse ,
    LangChainStream,
    experimental_StreamData} from 'ai';

import { BytesOutputParser } from 'langchain/schema/output_parser';
import { PromptTemplate } from 'langchain/prompts';
import {ChatOllama} from "langchain/chat_models/ollama";
import {ChromaClient} from "chromadb";
import {ConversationalRetrievalQAChain} from "langchain/chains";
import {collections, embeddings, models, setPrompt} from "@/utils/chat_utils";
import {Chroma} from "langchain/vectorstores/chroma";
import {ChatOpenAI} from "@langchain/openai";

export const runtime = 'edge';

export async function POST(req: NextRequest) {

    const data = new experimental_StreamData();

    const { stream, handlers } = LangChainStream({
        onFinal: () => {
            data.append(JSON.stringify({ key: 'value' })); // example
            data.close();
        },
        experimental_streamData: true,
    });

    const body = await req.json();

  
    const model = new ChatOpenAI({
            temperature : 0,
        })

    const chain =  ConversationalRetrievalQAChain.fromLLM(
        model,
        (await Chroma.fromExistingCollection(embeddings["openAi"], {collectionName: collections["openAi"]})).asRetriever(),
        {
            qaChainOptions: {
                type: "stuff",
                prompt: PromptTemplate.fromTemplate(setPrompt()),
            },
            returnSourceDocuments: true,
        }
    )

    await chain.stream({ question: "ciao" , chat_history : [] }, { callbacks: [handlers] });
    return new StreamingTextResponse(stream, {}, data);
}