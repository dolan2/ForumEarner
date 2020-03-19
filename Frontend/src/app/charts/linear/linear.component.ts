import {Component, Input} from '@angular/core';
import {Linear} from '../../models/linear.class';
import {environment} from '../../../environments/environment';

@Component({
  selector: 'app-linear',
  templateUrl: './linear.component.html',
  styleUrls: ['./linear.component.css']
})
export class LinearComponent {

  view: any[] = environment.view;

  @Input() data: Linear[];
  @Input() yAxisLabel: string;
  @Input() xAxisLabel: string;

  legend = true;
  animations = true;
  xAxis = true;
  yAxis = true;
  showYAxisLabel = true;
  showXAxisLabel = true;
  timeline = true;
  colorScheme = environment.colorScheme;

}
