import "./css/VideoCard.css";

const VideoCard = ({ title, description, thumbnailDefaultResolution, thumbnailHighResolution }) => {
  return (
    <div className="video-holder">
        <div className="video-thumb"><img alt={title} src={thumbnailHighResolution} /></div>
        <div className="video-content">
            <h3 className="video-title">{title}</h3>
            <p>{description}</p>
        </div>
    </div>
  );
};

export default VideoCard;
