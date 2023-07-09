import { Api } from '../gensrc/api/Api';
import { TestResponse } from '../gensrc/api/data-contracts';


const serviceBaseUrl = `${window.location.origin}`;
console.log(serviceBaseUrl);

const api = new Api( {
    baseUrl: "http://127.0.0.1:5000",
} );

export class MessageApi {
    static async getMessage(): Promise<TestResponse> {
        return await api.getHello()
        .then(
            (resp) => resp.data,
        )
        .catch(
            (err) => {
                console.log(err);
                return { 'message': '' }
            }
        );
    }
}