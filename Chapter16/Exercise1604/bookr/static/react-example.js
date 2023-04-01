class ClickCounter extends React.Component {
  constructor(props) {
    super(props);
    this.state = { clickCount: 0, name: props.name, target: props.target};
  }

  render() {
    if (this.state.clickCount === this.state.target) {
      return <span>Well done, {this.state.name}!</span>;
    }

    return <button onClick={() => this.setState({ 
           clickCount: this.state.clickCount + 1 
           }) 
      }>
	  {this.state.clickCount}
    </button>;
  }
}

class BookDisplay extends React.Component {
  constructor(props) {
    super(props);
    this.state = { books: [], url: props.url, fetchInProgress: false };
  }

  doFetch() {
    if (this.state.fetchInProgress)
        return;
    this.setState({ fetchInProgress: true })

    fetch(this.state.url, {
        method: 'GET',
        headers: {
            Accept: 'application/json'
         }
        }
    ).then((response) => {
        return response.json();
    }).then((data) => {
        this.setState({ fetchInProgress: false, books: data });
    })
  }

  render() {
    const bookListItems = this.state.books.map((book) => {
        return <li key={ book.pk }>{ book.title }</li>;
    })

    const buttonText = this.state.fetchInProgress  ? 'Fetch in Progress' : 'Fetch';

    return <div>
        <ul>{ bookListItems }</ul>
        <button onClick={ () => this.doFetch() } disabled={ this.state.fetchInProgress }>
            {buttonText}
        </button>
    </div>;
  }
}
