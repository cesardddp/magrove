class ToDoItem extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			is_done: false,
			//adding new key 'decoration' to change <li> style 
			decoration:{
				"text-decoration": "none"
			}
		}
		// bind this
		this.completeTask = this.completeTask.bind(this)
	}


	completeTask(){
		// create a new state reverting previous state
		// changing decoration (style) checking is_done value
		let new_state = {
			is_done : !this.state.is_done,
			decoration: !this.state.is_done ? {"text-decoration":"line-through"}
			: {"text-decoration": "none"}
		}
		// set new state
		this.setState(new_state)
	}

	render() {
		return (
			<li onClick={this.completeTask} style={this.state.decoration}>
				{this.props.task}
			</li>
		);
	}
}	

class ToDoList extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			to_do_list: ['Finish this test', 'Get hired', 'Change the world']
		};
		// bind this
		this.newTask = this.newTask.bind(this)
	}

	newTask(){
		// get task input text value
		let task = document.getElementById('input_text').value.trim()
		if (task==="") return 
		// create a reference from task list to call in setState function
		let old_to_do_list = this.state.to_do_list

		// push new task to the task list
		old_to_do_list.push(task)

		// change the state to adding new task
		this.setState({
			to_do_list:old_to_do_list
	});

	//clear input_text field
	document.getElementById('input_text').value = "";
}

	render() {
		return (
			<div>
				<h2>Add a new task to your to-do list</h2>
				<input type="text" id="input_text" />
				<button onClick={this.newTask} >Add</button>
				<ul>
					{this.state.to_do_list.map((task_text) =>
						<ToDoItem task={task_text} />
					)}
				</ul>
			</div>
		);
	}
}

ReactDOM.render(
	<ToDoList/>,
	document.getElementById('root')
);