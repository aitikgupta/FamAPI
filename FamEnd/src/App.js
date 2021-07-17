import { useState, useEffect } from 'react';

import Button from './Components/Button';
import Search from './Components/Search';
import VideoCard from './Components/VideoCard';

import { fetchLatest } from './service/Fetch';

import "./App.css";


function App() {
  const [result, setResult] = useState([]);
  const [query, setQuery] = useState("");
  const [currentPage, setCurrentPage] = useState(0);


  const getVideos = async (newPage) => {
    try {
        const { results } = await fetchLatest(newPage ?? currentPage, query);
        let videoCards = results.map(element => < VideoCard key = {
                element._id
            }
            title = {
                element.title
            }
            description = {
                element.description
            }
            thumbnailDefaultResolution = {
                element.thumbnail_defaultres
            }
            thumbnailHighResolution = {
                element.thumbnail_highres
            }
            />);
            console.log("[FamEnd] New results in!");
            console.log(videoCards);
            if (videoCards.length > 0) {
                setResult(videoCards);
            }
            else {
                setResult("No more results..")
            }
        }
        catch (error) {
            // something went wrong
            console.log("[FamEnd] Error: ", error);
        }
    }

  useEffect(() => {
    // fetch as soon as mounted
    getVideos();

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);


  const updatePage = (newPage) => {
      console.log("[FamEnd] Updating page:", newPage);
      setCurrentPage(newPage);
      getVideos(newPage);
  }

  const onClickHandler = () => {
      updatePage(currentPage + 1);
  }

  const pagination = <Button text={"Next ->"} onClickHandler={onClickHandler} />

  return (
    <div className="App">
        <header className="App-header"/>

        <Search query={query} setQuery={setQuery} getVideos={getVideos} />

        <div className="videoHolder">
            {result}
        </div>

        <div className="paginationHolder">
            {pagination}
        </div>
    </div>
  );
}

export default App;
