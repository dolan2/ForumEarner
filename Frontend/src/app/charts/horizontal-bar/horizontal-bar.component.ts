import {Component, Input, OnInit} from '@angular/core';
import {Post} from "../../models/post.interface";
import {HorizontalBar} from "../../models/horizontal-bar.interface";

@Component({
  selector: 'app-horizontal-bar',
  templateUrl: './horizontal-bar.component.html',
  styleUrls: ['./horizontal-bar.component.css']
})
export class HorizontalBarComponent implements OnInit {

  @Input() posts: Post[];
  data: HorizontalBar[];
  selectData: string[] = ['Age', 'Stack', 'Exp', 'Salary', 'Contract type', 'Location'];
  selected: string = 'Age';

  view: any[] = [1000, 600];
  showXAxis: boolean = true;
  showYAxis: boolean = true;
  gradient: boolean = false;
  showLegend: boolean = true;
  showXAxisLabel: boolean = true;
  showYAxisLabel: boolean = false;
  yAxisLabel: string = 'Age';
  xAxisLabel: string = 'Number of employees';
  colorScheme = {
    domain: ['#5AA454', '#A10A28', '#C7B42C', '#AAAAAA']
  };

  ngOnInit() {
    this.chartAge();
  }

  onSelectedData() {
    switch (this.selected) {
      case 'Age': {
        this.chartAge();
        break;
      }
      case 'Stack': {
        this.chartStack();
        break;
      }
      case 'Exp': {
        this.chartExp();
        break;
      }
      case 'Salary': {
        this.chartSalary();
        break;
      }
      case 'Contract type': {
        this.charContractType();
        break;
      }
      case 'Location': {
        this.chartLocation();
        break;
      }
    }
  }

  chartAge() {

    this.data = [
      new HorizontalBar('Younger than 15 years', 0),
      new HorizontalBar('15 to 19 years', 0),
      new HorizontalBar('20 to 24 years', 0),
      new HorizontalBar('25 to 29 years', 0),
      new HorizontalBar('30 to 34 years', 0),
      new HorizontalBar('35 to 39 years', 0),
      new HorizontalBar('40 to 44 years', 0),
      new HorizontalBar('45 to 49 years', 0),
      new HorizontalBar('50 to 54 years', 0),
      new HorizontalBar('55 to 59 years', 0),
      new HorizontalBar('60 years and older', 0)
    ];

    this.posts.forEach(post => {
      switch (true) {
        case (post.age < 15): {
          this.data.filter(x => x.name == 'Younger than 15 years').map(y => y.value += 1);
          break;
        }
        case (post.age >= 15 && post.age < 20): {
          this.data.filter(x => x.name == '15 to 19 years').map(y => y.value += 1);
          break;
        }
        case (post.age >= 20 && post.age < 25): {
          this.data.filter(x => x.name == '20 to 24 years').map(y => y.value += 1);
          break;
        }
        case (post.age >= 25 && post.age < 30): {
          this.data.filter(x => x.name == '25 to 29 years').map(y => y.value += 1);
          break;
        }
        case (post.age >= 30 && post.age < 35): {
          this.data.filter(x => x.name == '30 to 34 years').map(y => y.value += 1);
          break;
        }
        case (post.age >= 35 && post.age < 40): {
          this.data.filter(x => x.name == '35 to 39 years').map(y => y.value += 1);
          break;
        }
        case (post.age >= 40 && post.age < 45): {
          this.data.filter(x => x.name == '40 to 44 years').map(y => y.value += 1);
          break;
        }
        case (post.age >= 45 && post.age < 50): {
          this.data.filter(x => x.name == '45 to 49 years').map(y => y.value += 1);
          break;
        }
        case (post.age >= 50 && post.age < 55): {
          this.data.filter(x => x.name == '50 to 54 years').map(y => y.value += 1);
          break;
        }
        case (post.age >= 55 && post.age < 60): {
          this.data.filter(x => x.name == '55 to 59 years').map(y => y.value += 1);
          break;
        }
        case (post.age >= 60): {
          this.data.filter(x => x.name == '60 years and older').map(y => y.value += 1);
          break;
        }
      }
    });
  }

  chartStack() {
    this.data = [];
    const uniqueStack = new Set(this.posts.map(post => post.stack));

    uniqueStack.forEach(stack => {
      this.data.push(new HorizontalBar(stack, 0))
    });

    this.posts.forEach(post => {
      this.data.filter(x => x.name == post.stack).map(y => y.value +=1)
    });
    this.data.sort((m, n) => (m.value > n.value) ? -1 : 1);
  }

  chartExp() {

  }

  chartSalary() {

  }

  charContractType() {

  }

  chartLocation() {
    this.data = [
      new HorizontalBar('Other', 0),
      new HorizontalBar('Śląsk', 0),
      new HorizontalBar('Trójmiasto', 0)
    ];

    const uniqueStack = new Set(this.posts.map(post => post.location));

    uniqueStack.forEach(location => {
      if (location.indexOf('Other') >= 0){
        this.data.filter(x=> x.name == 'Other').map(y => y.value += 1)
      } else if(location.indexOf('Śląsk') >= 0) {
        this.data.filter(x=> x.name == 'Śląsk').map(y => y.value += 1)
      } else if(location.indexOf('Trójmiasto') >= 0) {
        this.data.filter(x=> x.name == 'Trójmiasto').map(y => y.value += 1)
      } else {
        this.data.push(new HorizontalBar(location, 0))
      }
    });

    this.posts.forEach(post => {
      this.data.filter(x => x.name == post.location).map(y => y.value +=1)
    });
    this.data.sort((m, n) => (m.value > n.value) ? -1 : 1);
  }

}
