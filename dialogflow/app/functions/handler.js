'use strict';
import { makeResponse } from '../lib/utils';
const {WebhookClient} = require('dialogflow-fulfillment');
const {Card, Suggestion} = require('dialogflow-fulfillment');



export const fullfillment = async (event) => {
  const body = JSON.parse(event.body)
  console.log("[debug]body", body)
  const queryResult = body.queryResult
  console.log("[debug]queryResult", queryResult)
  const contexts = queryResult.outputContexts
  console.log("[debug]contexts", contexts)

  const agent = new WebhookClient();

  // function welcome(agent) {
  //   agent.add(`Welcome to my agent!`);
  // }
 
  // function fallback(agent) {
  //   agent.add(`I didn't understand`);
  //   agent.add(`I'm sorry, can you try again?`);
  // }

  // function yourFunctionHandler(agent) {
  //    //console.log("[debug]agent:", agent);
  //    //console.log("[debug]agent.keys:", Object.keys(agent));
  //    console.log("[debug]agent.contexts:", agent.contexts);
  //    //console.log("[debug]agent.parameters:", agent.parameters);
     
  //    const genericContext = agent.contexts.filter(function(item){
  //    	if (item.name === "generic") { 
  //         return true; 
  //       } else { 
  //         return false;
  //       }
  //    });
  //   console.log("[debug]genericContext:", genericContext);
  // }

  //  agent.add(new Card({
  //        title: `COVID-19 Assessment Results`,
  //        imageUrl: 'https://developers.google.com/actions/images/badges/XPM_BADGING_GoogleAssistant_VER.png',
  //        text: `This is the body text of a card.  You can even use line\n  breaks and emoji! 💁`,
  //        buttonText: 'This is a button',
  //        buttonUrl: 'https://assistant.google.com/'
  //      }));
  //  agent.setContext({ name: 'weather', lifespan: 2, parameters: { city: 'Rome' }});
  
  // let intentMap = new Map();
  // intentMap.set('Default Welcome Intent', welcome);
  // intentMap.set('Default Fallback Intent', fallback);
  // intentMap.set('7_answerHasSymptoms', yourFunctionHandler);
  // agent.handleRequest(intentMap);

  try {
    return makeResponse(200, {"result": body})
  } catch (error) {
    console.log("error response", error)
    return makeResponse(500, error)
  }
}
