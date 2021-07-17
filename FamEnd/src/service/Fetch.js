import axios from 'axios';
import { SEARCH_URL } from './Config';

export const fetchLatest = async (page, query) => {
  try {
    let FETCH_URL = `${SEARCH_URL}?page=${page}`;
    if(query?.length) FETCH_URL += `&query=${query}`
    const { data } = await axios.get(FETCH_URL);
    return data;
  } catch (err) {
    // errors are handled in main component
    throw err;
  }
}
