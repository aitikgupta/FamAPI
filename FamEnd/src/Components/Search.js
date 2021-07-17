import Button from "./Button";
import "./css/Search.css";

function Search({ query, setQuery, getVideos }) {
  return (
    <div className="searchHolder">
        <input
        type="text" 
        name="Search"
        placeholder="Fam, put your query.." 
        className="inputHolder"
        value={query}
        onChange={({ target: {value} }) => setQuery(value)}
        />
        <Button text="FamSearch!" onClickHandler={() => getVideos(0)} />
    </div>
    );
};

export default Search;
